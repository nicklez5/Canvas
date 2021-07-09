import { ExecOptionsWithStringEncoding } from "child_process";

export class Course{
    constructor(){}
    public name: string;
    public id: number;
    public lectures: any[];
    public students: any[];
    public assignments: any[];
}
export class Lecture{
    constructor(){}
    public description: string;
    public date_created: string;
    public name: string;
    public imageFile: string;
    public id: number;
    public course: any;
}

export class Assignment{
    constructor(){}
    public course: any;
    public name: string;
    public date_created: string;
    public student_points: number;
    public max_points: number;
    public date_due: string;
    public description: string;
    public id: number;
}

export class UserProfile{
    constructor(){}
    public id: number;
    public user: any;
    public first_name: string;
    public last_name: string;
    public phone_number: string;
    public age: number;
    public gender: string;
}

export class Student{
    constructor(){}
    public id: number;
    public profile: any;
    public assignments: any[];
}