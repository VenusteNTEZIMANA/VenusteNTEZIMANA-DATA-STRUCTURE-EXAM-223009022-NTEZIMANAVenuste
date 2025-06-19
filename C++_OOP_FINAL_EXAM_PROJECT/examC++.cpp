#include <iostream>
#include <vector>
#include <cstring>
#include <iomanip>
using namespace std;

// ===== Task 1: Define Student =====
struct Student {
    char name[30];
    float* grades;
    int nGrades;

    Student(const char* studentName, int numGrades) {
        strncpy(name, studentName, 29);
        name[29] = '\0';
        nGrades = numGrades;
        grades = new float[nGrades];
    }

    ~Student() {
        delete[] grades;
    }
};

// ===== Task 2: Abstract Metric Base Class =====
class Metric {
public:
    virtual float compute(const Student* s) = 0;
    virtual ~Metric() {}
};

class MeanMetric : public Metric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0;
        float sum = 0;
        for (int i = 0; i < s->nGrades; ++i)
            sum += *(s->grades + i); // Pointer arithmetic
        return sum / s->nGrades;
    }
};

class MinMetric : public Metric {
public:
    float compute(const Student* s) override {
        if (s->nGrades == 0) return 0;
        float minVal = *(s->grades);
        for (int i = 1; i < s->nGrades; ++i)
            if (*(s->grades + i) < minVal) // Pointer arithmetic
                minVal = *(s->grades + i);
        return minVal;
    }
};

// ===== Task 4: Grade Management =====
void addGrade(Student& s, float grade) {
    float* newGrades = new float[s.nGrades + 1];
    for (int i = 0; i < s.nGrades; ++i)
        *(newGrades + i) = *(s.grades + i); // Pointer arithmetic
    *(newGrades + s.nGrades) = grade;
    delete[] s.grades;
    s.grades = newGrades;
    s.nGrades++;
}

void removeGrade(Student& s, int index) {
    if (index < 0 || index >= s.nGrades) return;
    float* newGrades = new float[s.nGrades - 1];
    for (int i = 0, j = 0; i < s.nGrades; ++i) {
        if (i != index)
            *(newGrades + j++) = *(s.grades + i); // Pointer arithmetic
    }
    delete[] s.grades;
    s.grades = newGrades;
    s.nGrades--;
}

void printGrades(const Student& s) {
    cout << "Grades for " << s.name << ": ";
    for (int i = 0; i < s.nGrades; ++i)
        cout << *(s.grades + i) << " "; // Pointer arithmetic
    cout << endl;
}

void printGradesWithIndices(const Student& s) {
    cout << "Grades for " << s.name << ":\n";
    for (int i = 0; i < s.nGrades; ++i)
        cout << "[" << i << "] " << *(s.grades + i) << endl; // Pointer arithmetic
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
    return students[index];
}

// ===== Main Menu and Application Logic =====
int main() {
    vector<Student*> students;

    // Metric storage as Metric* array (polymorphism)
    Metric** metrics = new Metric*[2];
    metrics[0] = new MeanMetric();
    metrics[1] = new MinMetric();

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

        if (choice == 0) break;

        switch (choice) {
            case 1: {
                char name[30];
                int n;
                cout << "Enter student name: ";
                cin.ignore();
                cin.getline(name, 30);
                cout << "How many grades? ";
                cin >> n;

                Student* student = new Student(name, n);
                for (int i = 0; i < n; ++i) {
                    cout << "Enter grade " << i + 1 << ": ";
                    cin >> student->grades[i];
                }
                students.push_back(student);
                break;
            }

            case 2: {
                Student* s = selectStudent(students);
                if (!s) break;
                float grade;
                cout << "Enter grade to add: ";
                cin >> grade;
                addGrade(*s, grade);
                printGrades(*s);
                break;
            }

            case 3: {
                Student* s = selectStudent(students);
                if (!s) break;
                printGradesWithIndices(*s);
                int index;
                cout << "Enter index to remove (0-based): ";
                cin >> index;
                if (index >= 0 && index < s->nGrades) {
                    cout << "Removing grade: " << *(s->grades + index) << endl;
                    removeGrade(*s, index);
                } else {
                    cout << "Invalid grade index.\n";
                }
                break;
            }

            case 4: {
                Student* s = selectStudent(students);
                if (!s) break;
                cout << "Mean: " << fixed << setprecision(2)
                     << metrics[0]->compute(s) << endl;
                break;
            }

            case 5: {
                Student* s = selectStudent(students);
                if (!s) break;
                cout << "Min: " << fixed << setprecision(2)
                     << metrics[1]->compute(s) << endl;
                break;
            }

            case 6: {
                if (students.empty()) {
                    cout << "No students available.\n";
                    break;
                }
                for (auto s : students) {
                    cout << "Student: " << s->name << endl;
                    printGrades(*s);
                    cout << endl;
                }
                break;
            }

            default:
                cout << "Invalid option.\n";
        }
    }

    // Cleanup
    for (auto s : students) delete s;
    delete metrics[0];
    delete metrics[1];
    delete[] metrics;

    cout << "Exiting program.\n";
    return 0;
}

