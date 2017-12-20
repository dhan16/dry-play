import { Component, OnInit } from '@angular/core';
import { AuthHttp } from 'angular2-jwt';
import {Http, Response} from '@angular/http';
import { AuthService } from './../auth/auth.service';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';

@Component({
  selector: 'app-ping',
  templateUrl: './ping.component.html',
  styleUrls: ['./ping.component.css']
})
export class PingComponent implements OnInit {

  API_URL = 'http://localhost:3010/api';
  message: string;

  constructor(public auth: AuthService, public http: Http, public authHttp: AuthHttp) {}

  ngOnInit() {
  }

  private handle(response: Observable<Response>): void {
    response.map(res => {console.log(res); return res.text(); })
      .subscribe(
        message => this.message = message,
        error => this.message = error
      );
}

  public ping(): void {
    this.message = '';
    this.handle(this.http.get(`${this.API_URL}/public/`));
  }

  public securedPing(): void {
    this.message = '';
    this.handle(this.authHttp.get(`${this.API_URL}/private/`));
  }

  public readMessages(): void {
    this.message = '';
    this.handle(this.authHttp.get(`${this.API_URL}/private_read_messages/`));
  }

  public readGroupMessages(): void {
    this.message = '';
    this.handle(this.authHttp.get(`${this.API_URL}/private_read_groupmessages/`));
  }
}
