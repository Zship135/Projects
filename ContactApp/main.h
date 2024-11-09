#pragma once
#include <iostream>
#include<array> 
#include <vector>
#include <string> 
#include <fstream> 
using namespace std;

int main() {
	int x;
	string command("");

	struct Contact {
		string name;
		string company;
		string email;
		string location;
		string mobile_number;
		string office_number;
		string extension;
	};

	vector<Contact> contacts;

	ofstream file("save.txt");
	


	string name("");
	string company("");
	string email("");
	string location("");
	string mobile_number("");
	string office_number("");
	string extension("");
	string myText;
	bool running = true;
	cout << "Welcome to your contact book! For a list of commands, type /help.\n";


	while (running) {

		cin >> command;

		cin.ignore();

		if (command == "/help") {
			cout << "Here is a list of commands:\n";
			cout << "/list : lists all of your current contacts\n";
			cout << "/clear : clears the terminal\n";
			cout << "/add : fill in information to add a new contact\n";
			cout << "\n";
		}

		if (command == "/list") {
			cout << "Here is a list of your contacts:\n";

			for (Contact contact : contacts) {
				cout << contact.name + ", " + contact.company + ", " + contact.email + ", " + contact.location + ", " + contact.mobile_number + ", " + contact.office_number + ", " + contact.extension + "\n";
			}

			while (getline(file, myText)) {
				cout << myText;
			}
			
		}

		if (command == "/clear") {
			cout << "clearing...";
			system("cls");
			cout << "Welcome to your contact book! For a list of commands, type /help.\n";
		}

		if (command == "/add") {
			Contact new_contact;


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

			file << new_contact.name + ", " + new_contact.company + ", " + new_contact.email + ", " + new_contact.location + ", " + new_contact.mobile_number + 
				", " + new_contact.office_number + ", " + new_contact.extension + "\n";
		}
	}
	return 0;
}

