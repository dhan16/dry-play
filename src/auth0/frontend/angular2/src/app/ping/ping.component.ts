import { Component, OnInit } from '@angular/core';
import { AuthHttp } from 'angular2-jwt';
import { Http } from '@angular/http';
import { AuthService } from './../auth/auth.service';
import 'rxjs/add/operator/map';

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

  public ping(): void {
    this.message = '';
    this.http.get(`${this.API_URL}/public/`)
      .map(res => {console.log(res); return res.text(); })
      .subscribe(
        message => this.message = message,
        error => this.message = error
      );
  }

  public securedPing(): void {
    this.message = '';
    this.authHttp.get(`${this.API_URL}/private/`)
      .map(res => {console.log(res); return res.json(); })
      .subscribe(
        data => {console.log(data); this.message = data.message; },
        error => {console.log(error); this.message = error; },
      );
  }
}
