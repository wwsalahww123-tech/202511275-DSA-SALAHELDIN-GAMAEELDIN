#include <iostream>
#include <string>

using namespace std;

struct FamilyMember {
    string name;
    int age;
};

int main() {
    int n;
    cout << "Enter number of family members: ";
    cin >> n;

    FamilyMember family[100];
    for (int i = 0; i < n; i++) {
        cout << "Enter name and age: ";
        cin >> family[i].name >> family[i].age;
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (family[j].name > family[j + 1].name) {
                FamilyMember temp = family[j];
                family[j] = family[j + 1];
                family[j + 1] = temp;
            }
        }
    }

    string key;
    cout << "Enter a key name to be searched: ";
    cin >> key;

    int low = 0, high = n - 1;
    bool found = false;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (family[mid].name == key) {
            cout << "name was found and is aged " << family[mid].age << endl;
            found = true;
            break;
        }
        else if (family[mid].name < key) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    if (!found) cout << "Not found" << endl;

    string names[] = {"Zuck", "Shayd", "Emely", "Amjed", "Esther", "Manar", "Anne"};
    int namesSize = 7;
    for (int i = 0; i < namesSize - 1; i++) {
        for (int j = 0; j < namesSize - i - 1; j++) {
            if (names[j] > names[j + 1]) {
                string temp = names[j];
                names[j] = names[j + 1];
                names[j + 1] = temp;
            }
        }
    }
    cout << "\nSorted Names: ";
    for (int i = 0; i < namesSize; i++) cout << names[i] << " ";
    cout << endl;

    int nums[] = {109, 99, 23, 45, 23, 2, 5, 1};
    int numsSize = 8;
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = 0; j < numsSize - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                int temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
    }
    cout << "\nSorted Numbers: ";
    for (int i = 0; i < numsSize; i++) cout << nums[i] << " ";
    cout << endl;

    return 0;
}
