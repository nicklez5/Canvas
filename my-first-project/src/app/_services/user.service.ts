import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Course } from '../models';
const API_URL = 'http://localhost:8080/api/';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private _course_url: string = "http://127.0.0.1:8000/api/course/";
  private _lecture_url: string = "http://127.0.0.1:8000/api/lecture/";
  private _assignment_url: string = "http://127.0.0.1:8000/api/assignment/";
  private _student_url: string = "http://127.0.0.1:8000/api/student/";
  private _profile_url: string = "http://127.0.0.1:8000/api/profile/";
  constructor(private http: HttpClient) { }

  getUserCourses(): Observable<any> {
    return this.http.get(this._url + 'courses', { responseType: 'text' });
  }

  getModeratorBoard(): Observable<any> {
    return this.http.get(API_URL + 'mod', { responseType: 'text' });
  }

  getAdminBoard(): Observable<any> {
    return this.http.get(API_URL + 'admin', { responseType: 'text' });
  }
}
