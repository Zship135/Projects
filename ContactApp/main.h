#pragma once
#include <iostream>
using namespace std;

int main() {
	int x;
	string command("");
	string contacts[1] = {};
	bool running = true;
	cout << "Welcome to your contact book! For a list of commands, type /help.\n";
	while (running) {
		
		cin >> command;
		if (command == "/help") {
			cout << "Here is a list of commands:\n";
		}

		if (command == "/list") {
			cout << "Here is a list of your contacts:\n";
			cout << contacts, "\n";
		}

		if (command == "/clear") {
			cout << "clearing...";
			system("cls");
			cout << "Welcome to your contact book! For a list of commands, type /help.\n";
		}
	}
	return 0;
}

