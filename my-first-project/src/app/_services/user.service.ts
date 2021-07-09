import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Course, Lecture, Assignment, UserProfile, Student } from '../models';
const API_URL = 'http://127.0.0.1:8080/api/';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor(private http: HttpClient) { }

  //Courses
  getCourses(): Observable<Course[]> {
    return this.http.get<Course[]>(API_URL + 'courses/').pipe(catchError(this.errorHandler));
  }
  errorHandler(error: HttpErrorResponse){
    return throwError(error.message || "Server Error")
  }
  getCourseById(id:number): Observable<Course[]>{
    return this.http.get<Course[]>(API_URL + 'courses/' + id).pipe(catchError(this.errorHandler));
  }
  postCourse(empData: any): Observable<Course[]>{
    return this.http.post<Course[]>(API_URL + 'courses/', empData).pipe(catchError(this.errorHandler));
  }

  updateCourse(id:number, empData: any): Observable<Course[]>{
    return this.http.put<Course[]>(API_URL + 'courses/' + id,empData).pipe(catchError(this.errorHandler));
  }

  deleteCourse(id: any){
    return this.http.delete(API_URL + 'courses/'+  id);
  }

  //Lectures 
  getLectures(): Observable<Lecture[]> {
    return this.http.get<Lecture[]>(API_URL + 'lectures/').pipe(catchError(this.errorHandler));
  }

  getLectureById(id:number): Observable<Lecture[]>{
    return this.http.get<Lecture[]>(API_URL + 'lectures/' + id).pipe(catchError(this.errorHandler));
  }

  postLecture(empData: any): Observable<Lecture[]>{
    return this.http.post<Lecture[]>(API_URL + 'lectures/', empData).pipe(catchError(this.errorHandler));
  }

  updateLecture(id:number, empData: any): Observable<Lecture[]>{
    return this.http.put<Lecture[]>(API_URL + 'lectures/' + id,empData).pipe(catchError(this.errorHandler));
  }

  deleteLecture(id: any){
    return this.http.delete(API_URL + 'lectures/'+  id);
  }

  //Assignment
  getAssignments(): Observable<Assignment[]> {
    return this.http.get<Assignment[]>(API_URL + 'assignments/').pipe(catchError(this.errorHandler));
  }

  getAssignmentById(id:number): Observable<Assignment[]>{
    return this.http.get<Assignment[]>(API_URL + 'assignments/' + id).pipe(catchError(this.errorHandler));
  }

  postAssignment(empData: any): Observable<Assignment[]>{
    return this.http.post<Assignment[]>(API_URL + 'assignments/', empData).pipe(catchError(this.errorHandler));
  }

  updateAssignment(id:number, empData: any): Observable<Assignment[]>{
    return this.http.put<Assignment[]>(API_URL + 'assignments/' + id,empData).pipe(catchError(this.errorHandler));
  }

  deleteAssignment(id: any){
    return this.http.delete(API_URL + 'assignments/'+  id);
  }
  
}
