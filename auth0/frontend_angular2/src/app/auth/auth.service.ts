﻿import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import 'rxjs/add/operator/filter';
import * as auth0 from 'auth0-js';
import {environment} from '../../environments/environment';
import {Auth0DecodedHash} from 'auth0-js';

@Injectable()
export class AuthService {

  auth0 = new auth0.WebAuth({
    clientID: environment.auth0.clientID,
    domain: environment.auth0.domain,
    redirectUri: environment.auth0.callbackURL,
    audience: environment.auth0.audience,
    responseType: 'token id_token',
    scope: 'openid profile' // permissions are added to returned scope by the rule in access_token_scopes_rule.txt
  });

  userProfile: any;

  constructor(public router: Router) {}

  public login(): void {
    this.auth0.authorize();
  }

  public handleAuthentication(navigateTo = ['/']): void {
    this.auth0.parseHash((err: any, authResult: any) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        window.location.hash = '';
        this.setSession(authResult);
        this.router.navigate(navigateTo);
      } else if (err) {
        this.router.navigate(navigateTo);
        console.log(err);
        alert(`Error: ${err.error}. ${err.errorDescription}`);
      }
    });
  }

  public getUsername(): string {
    return localStorage.getItem('username');
  }

  public getNickname(): string {
    return localStorage.getItem('nickname');
  }

  private getToken() {
    return localStorage.getItem('access_token');
  }

  public getAuthorizationHeader() {
    return environment.JWT_AUTH_HEADER_PREFIX + ' ' + this.getToken();
  }

  public getProfile(cb: any): void {
    const accessToken = this.getToken();
    const self = this;
    this.auth0.client.userInfo(accessToken, (err: any, profile: any) => {
      if (profile) {
        self.userProfile = profile;
      }
      cb(err, profile);
    });
  }

  public loginAsGuest(navigateTo = ['/']): void {
    let expiresInSecs = 24 * 60 * 60;
    this.setSessionDetails(`guest`, expiresInSecs, 'guest', 'guest');
    this.router.navigate(navigateTo);
  }

  private setSession(authResult: Auth0DecodedHash): void {
    this.setSessionDetails(authResult.accessToken, authResult.expiresIn, authResult.idTokenPayload['sub'],
      authResult.idTokenPayload['nickname']);
  }

  private setSessionDetails(accessToken: string, expiresInSecs: number, username: string, nickname: string): void {
    // Set the time that the access token will expire at
    const expiresAt = JSON.stringify((expiresInSecs * 1000) + new Date().getTime());
    localStorage.setItem('access_token', accessToken);
    localStorage.setItem('username', username);
    localStorage.setItem('nickname', nickname);
    localStorage.setItem('expires_at', expiresAt);
  }

  public logout(): void {
    // Remove tokens and expiry time from localStorage
    localStorage.removeItem('access_token');
    localStorage.removeItem('username');
    localStorage.removeItem('nickname');
    localStorage.removeItem('expires_at');
    // logout from auth0
    this.auth0.logout({
      returnTo: environment.auth0.callbackURL
    });
  }

  public isAuthenticated(): boolean {
    // Check whether the current time is past the
    // access token's expiry time
    const expiresAt = JSON.parse(localStorage.getItem('expires_at'));
    return new Date().getTime() < expiresAt;
  }
}
