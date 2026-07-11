#include <iostream>
using namespace std;

int main() {
    int rollno;
    char name[50];
    float marks;

    cout << "enter roll number: ";
    cin >> rollno;

    cout << "enter student name: ";
    cin >> name;

    cout << "enter marks: ";
    cin >> marks;

    cout << "\nstudent information" << endl;
    cout << "roll number: " << rollno << endl;
    cout << "name: " << name << endl;
    cout << "marks: " << marks << endl;

    return 0;
}