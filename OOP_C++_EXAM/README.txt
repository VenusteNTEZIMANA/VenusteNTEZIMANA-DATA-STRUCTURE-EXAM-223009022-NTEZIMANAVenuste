Student Grade Metrics

The primary objective of this project, Student Grade Metrics, is to design and implement a C++ application that allows users to manage student records and compute specific grade metrics using dynamic memory and object-oriented programming principles.
This project aims to:
 Represent student data using structures, including dynamically allocated arrays for grades.
Demonstrate polymorphism by designing a metric system where different grading metrics (like mean and minimum) are implemented through inheritance from a common abstract base class.
 Utilize pointer arithmetic to operate on dynamically allocated grade arrays.
 Provide interactive functionality to add or remove grades, view metrics, and manage multiple students through a console menu.
Apply proper memory management by ensuring that all dynamically allocated memory is correctly cleaned up to prevent memory leaks
I.  Assigned Task
The assigned task, as described in the "Student Grade Metrics: Explanation" document, involved creating a C++ program with the following key objectives:

1.Define a `Student` struct:This struct needed to manage student names and dynamically allocated arrays of their grades. This included implementing a constructor for proper initialization and a destructor for memory cleanup.
2.  Implement an abstract `Metric` base class:This class was designed to serve as an interface for different grade calculation methods. Derived classes, `MeanMetric` and `MinMetric`, were then created to compute the average and minimum grades, respectively, demonstrating inheritance and polymorphism.
3.  Utilize polymorphic storage for metrics: The program was required to store `Metric` pointers in a `Metric**` array, showcasing how polymorphism allows calling the correct `compute` method at runtime.
4.  Employ pointer arithmetic: All operations involving the `grades` array (calculating metrics, adding, and removing grades) needed to explicitly use pointer arithmetic instead of array indexing.
5.  Implement grade management functions: Functions for adding (`addGrade`) and removing (`removeGrade`) grades dynamically by resizing the grade array were required.
6.  Ensure robust memory management: Proper allocation and deallocation of all dynamic memory (for `Student` objects, grade arrays, `Metric` objects, and the `metrics` array) was crucial to prevent memory leaks.

II. How the Task Was Completed
This project was developed using C++ and follows object-oriented programming principles, dynamic memory management, and user interaction through a console-based menu. Here's a breakdown of how each task from the assignment was completed:
1. Student Structure with Dynamic Grade Allocation
A Student structure was created to store each student's name, their list of grades, and the number of grades they have. Instead of using fixed-size arrays for grades, dynamic memory allocation was used. This means that when a student is created, the memory for their grades is allocated at runtime based on how many grades the user wants to enter.
2. Abstract Metric Class and Inheritance
An abstract base class named Metric was defined. This class includes a pure virtual function, meaning that any class derived from it must implement this function. Two metric types were created:
MeanMetric: Calculates the average of a student’s grades.
MinMetric: Determines the minimum grade from the list.
Both classes inherit from Metric, demonstrating the use of inheritance and polymorphism.
3. Polymorphism and Metric Array
To demonstrate polymorphism, an array of pointers to the Metric base class was used. This allows the program to treat both MeanMetric and MinMetric objects uniformly, storing them in a single array. When the user chooses to compute a metric, the correct computation method is automatically called based on the actual type of the object, even though it is accessed through a base class pointer.
4. Pointer Arithmetic
Instead of using traditional array indexing, all metric calculations and grade manipulations are done using pointer arithmetic. This involves navigating through the grade array using memory address manipulation, which reinforces understanding of low-level operations in C++.
5. Grade Addition and Removal Functions
Two functions were implemented to manage grades:
Add Grade: This creates a new dynamic array one element larger than the current one, copies the existing grades, adds the new grade at the end, deletes the old array, and updates the student’s grade pointer.
Remove Grade: This does the reverse—creates a new array one element smaller, skips the grade to be removed while copying, deletes the old array, and updates the student's grade pointer.
These functions ensure that memory is properly managed each time grades are added or removed.
6. Menu-Based User Interface
The program features a loop-driven text menu that allows users to interact with the system. Options include:
Adding a new student and entering grades
Adding or removing a grade for an existing student
Viewing computed mean or minimum grade
Displaying all student names and their grades
The menu ensures an intuitive experience and keeps users informed of available operations.
7. Memory Management
Dynamic memory was used throughout the program for student grades, student objects, and metric objects. Before the program exits, all dynamically allocated memory is properly deleted. This prevents memory leaks and demonstrates responsible resource management.
III. Annotated Code with comments
#include <iostream>     // For standard I/O operations
#include <vector>       // For using std::vector to store multiple students
#include <cstring>      // For string copy with strncpy
#include <iomanip>      // For controlling output format (setprecision)
using namespace std;;
// ===== Task 1: Define Student =====
struct Student {
    char name[30];         // Array to store student's name (up to 29 characters + null terminator)
    float* grades;         // Pointer to dynamically allocated array of grades
    int nGrades;           // Number of grades for the student

    Student(const char* studentName, int numGrades) {
        strncpy(name, studentName, 29); // Copy the name into the name array (safe copy)
        name[29] = '\0';                          // Ensures null termination
        nGrades = numGrades;            // Store the number of grades
        grades = new float[nGrades];    // Dynamically allocate memory for grades
    }
Student() {
        delete[] grades;                // Frees memory when the Student object is destroyed
    }
};
// ===== Task 2: Abstract Metric Base Class =====
class Metric {
public:
    virtual float compute(const Student* s) = 0;  // Pure virtual function to be implemented by derived classes
    virtual ~Metric() {}                          // Virtual destructor to ensure proper cleanup in inheritance
};
// ===== Derived Metric Classes =====
class MeanMetric : public Metric {
public:
    float compute(const Student* s) override {
if (s->nGrades == 0) return 0;            // Handle case with no grades
        float sum = 0;
        for (int i = 0; i < s->nGrades; ++i)
            sum += *(s->grades + i);              // Add each grade using pointer arithmetic
        return sum / s->nGrades;               // Return mean value
 }
};
class MinMetric : public Metric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0;            // Handle empty grade list
        float minVal = *(s->grades);              // Assume first grade is minimum
        for (int i = 1; i < s->nGrades; ++i)
            if (*(s->grades + i) < minVal)        // Compare using pointer arithmetic
                minVal = *(s->grades + i);        // Update minimum if smaller grade found
        return minVal;
    }
};
// ===== Task 4: Grade Management =====
void addGrade(Student& s, float grade) {
    float* newGrades = new float[s.nGrades + 1];     // Allocate new array with one extra slot
    for (int i = 0; i < s.nGrades; ++i)
        *(newGrades + i) = *(s.grades + i);          // Copy existing grades using pointer arithmetic
    *(newGrades + s.nGrades) = grade;         // Add the new grade
    delete[] s.grades;                                 // Free old memory
    s.grades = newGrades;                        // Update pointer to the new grades array
    s.nGrades++;                                     // Increment grade count
}
void removeGrade(Student& s, int index) {
    if (index < 0 || index >= s.nGrades) return;     // Check for invalid index
    float* newGrades = new float[s.nGrades - 1];     // Allocate new array with one less slot
 for (int i = 0, j = 0; i < s.nGrades; ++i) {
        if (i != index)
            *(newGrades + j++) = *(s.grades + i);    // Copy all except the one at 'index'
    }
    delete[] s.grades;                               // Free old memory
    s.grades = newGrades;                            // Update pointer
    s.nGrades--;                                     // Decrement grade count
}

void printGrades(const Student& s) {
    cout << "Grades for " << s.name << ": ";
    for (int i = 0; i < s.nGrades; ++i)
        cout << *(s.grades + i) << " ";              // Print each grade using pointer arithmetic
    cout << endl;
}
void printGradesWithIndices(const Student& s) {
    cout << "Grades for " << s.name << ":\n";
    for (int i = 0; i < s.nGrades; ++i)
        cout << "[" << i << "] " << *(s.grades + i) << endl; // Print index and grade
}
// ===== Task 5: Student Menu and Management =====
void listStudents(const vector<Student*>& students) {
    cout << "Available students:\n";
    for (size_t i = 0; i < students.size(); ++i)
cout << i << ". " << students[i]->name << endl;
}
Student* selectStudent(vector<Student*>& students) {
    if (students.empty()) {
        cout << "No students available.\n";
        return nullptr;
    }
    listStudents(students);
    int index;
    cout << "Select student index: ";
    cin >> index;
    if (index < 0 || index >= (int)students.size()) {
        cout << "Invalid student index.\n";
        return nullptr;
    }
    return students[index]; // Return pointer to selected student
}

// ===== Main Menu and Application Logic =====
int main() {
    vector<Student*> students;                  // Vector to store all student records

    Metric** metrics = new Metric*[2];          // Array of pointers to Metric objects
    metrics[0] = new MeanMetric();              // Assign MeanMetric to index 0
    metrics[1] = new MinMetric();               // Assign MinMetric to index 1

    int choice;
    while (true) {
        cout << "\n========== MENU Student Grade System ==========\n";
        cout << "1. Enter new student and grades\n";
        cout << "2. Add a grade to a student\n";
        cout << "3. Remove a grade from a student\n";
        cout << "4. View student grade mean\n";
        cout << "5. View student grade min\n";
        cout << "6. Show all student names and grades\n";
        cout << "0. Exit\n";
        cout << "===============================================\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 0) break;                 // Exit condition

        switch (choice) {
            case 1: {
                char name[30];
                int n;
                cout << "Enter student name: ";
                cin.ignore();                  // Clear buffer before getline
                cin.getline(name, 30);         // Read full line into name
                cout << "How many grades? ";
                cin >> n;

                Student* student = new Student(name, n); // Create new student
                for (int i = 0; i < n; ++i) {
                    cout << "Enter grade " << i + 1 << ": ";
                    cin >> student->grades[i]; // Input each grade
                }
                students.push_back(student);   // Add student to list
                break;
            }

     case 2: {
                Student* s = selectStudent(students);  // Select a student
                if (!s) break;
                float grade;
                cout << "Enter grade to add: ";
                cin >> grade;
                addGrade(*s, grade);                  // Call add function
                printGrades(*s);                      // Show updated grades
                break;
            }
        case 3: {
                Student* s = selectStudent(students);
                if (!s) break;
                printGradesWithIndices(*s);           // Show grades with indices
                int index;
                cout << "Enter index to remove (0-based): ";
                cin >> index;
                if (index >= 0 && index < s->nGrades) {
                    cout << "Removing grade: " << *(s->grades + index) << endl;
                    removeGrade(*s, index);           // Remove selected grade
                } else {
                    cout << "Invalid grade index.\n";
                }
                break;
            }

            case 4: {
                Student* s = selectStudent(students);
                if (!s) break;
                cout << "Mean: " << fixed << setprecision(2)
                     << metrics[0]->compute(s) << endl;  // Compute mean
                break;
            }
case 5: {
                Student* s = selectStudent(students);
                if (!s) break;
                cout << "Min: " << fixed << setprecision(2)
                     << metrics[1]->compute(s) << endl;  // Compute min
                break;
            }
case 6: {
                if (students.empty()) {
                    cout << "No students available.\n";
                    break;
                }
                for (auto s : students) {
                    cout << "Student: " << s->name << endl;
                    printGrades(*s);                  // Display each student's grades
                    cout << endl;
                }
                break;
            }
default:
                cout << "Invalid option.\n";          // Catch invalid choices
        } }
for (auto s : students) delete s;           // Cleanup student memory
    delete metrics[0];
    delete metrics[1];
    delete[] metrics;

    cout << "Exiting program.\n";                    // Exit message
    return 0;                                        // End program
}
