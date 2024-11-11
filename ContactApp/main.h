#pragma once
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct Contact {
    string name;
    string company;
    string email;
    string location;
    string mobile_number;
    string office_number;
    string extension;
};

int main() {
    vector<Contact> contacts;
    string command;
    int remove;
    string filename = "contacts.txt";

    // Load contacts from file
    ifstream infile(filename);
    if (infile.is_open()) {
        Contact contact;
        while (getline(infile, contact.name, ',') &&
            getline(infile, contact.company, ',') &&
            getline(infile, contact.email, ',') &&
            getline(infile, contact.location, ',') &&
            getline(infile, contact.mobile_number, ',') &&
            getline(infile, contact.office_number, ',') &&
            getline(infile, contact.extension)) {
            contacts.push_back(contact);
        }
        infile.close();
    }
    else {
        cout << "Could not open the file for reading.\n";
    }

    cout << "Welcome to your contact book! For a list of commands, type /help.\n";

    bool running = true;
    while (running) {
        cin >> command;
        cin.ignore();

        if (command == "/help") {
            cout << "\n";
            cout << "Here is a list of commands:\n";
            cout << "/list : lists all of your current contacts\n";
            cout << "/clear : clears the terminal\n";
            cout << "/add : fill in information to add a new contact\n";
            cout << "/exit : exit the contact book application\n";
            cout << "\n";
        }
        else if (command == "/list") {
            cout << "Here is a list of your contacts:\n";
            int i = 1;
            for (const Contact& contact : contacts) {
                
                cout << "[" << i << "] " << contact.name << ", " << contact.company << ", " << contact.email << ", "
                    << contact.location << ", " << contact.mobile_number << ", "
                    << contact.office_number << ", " << contact.extension << "\n";
                i++;
            }
        }
        else if (command == "/clear") {
            #ifdef _WIN32
                system("cls");
            #else
                system("clear");
            #endif

            cout << "Welcome to your contact book! For a list of commands, type /help.\n";
        }
        else if (command == "/add") {
            Contact new_contact;

            cout << "\n";
            cout << "Enter information to add a contact:\n";
            cout << "Name: ";
            getline(cin, new_contact.name);
            cout << "Company: ";
            getline(cin, new_contact.company);
            cout << "Email: ";
            getline(cin, new_contact.email);
            cout << "Location: ";
            getline(cin, new_contact.location);
            cout << "Mobile Phone: ";
            getline(cin, new_contact.mobile_number);
            cout << "Office Phone: ";
            getline(cin, new_contact.office_number);
            cout << "Extension: ";
            getline(cin, new_contact.extension);

            contacts.push_back(new_contact);

            // Append the new contact to the file
            ofstream outfile(filename, ios::app);
            if (outfile.is_open()) {
                outfile << new_contact.name << "," << new_contact.company << "," << new_contact.email << ","
                    << new_contact.location << "," << new_contact.mobile_number << ","
                    << new_contact.office_number << "," << new_contact.extension << endl;
                outfile.close();
                cout << "Contact added successfully.\n";
                cout << "\n";
            }
            else {
                cout << "Could not open the file for writing.\n";
                cout << "\n";
            }
        }
        else if (command == "/exit") {
            cout << "Exiting the contact book. Goodbye!\n";
            running = false;
        }
        else if (command == "/remove") {
            cout << "\n";
            cout << "Type the number of the contact you would like to remove: \n";
            cout << "\n";

            int i = 1;
            for (const Contact& contact : contacts) {

                cout << "[" << i << "] " << contact.name << ", " << contact.company << ", " << contact.email << ", "
                    << contact.location << ", " << contact.mobile_number << ", "
                    << contact.office_number << ", " << contact.extension << "\n";
                i++;
            }

            cin >> remove;
            contacts.erase(contacts.begin() + (remove - 1));

            ofstream outfile(filename, ios::trunc);
            outfile.close();

            ifstream infile(filename);
            if (infile.is_open()) {
                Contact contact;
                while (getline(infile, contact.name, ',') &&
                    getline(infile, contact.company, ',') &&
                    getline(infile, contact.email, ',') &&
                    getline(infile, contact.location, ',') &&
                    getline(infile, contact.mobile_number, ',') &&
                    getline(infile, contact.office_number, ',') &&
                    getline(infile, contact.extension)) {
                    contacts.push_back(contact);
                }
                infile.close();
            }




        }
        else {
            cout << "Unknown command. Type /help for a list of available commands.\n";
        }
    }

    return 0;
}
