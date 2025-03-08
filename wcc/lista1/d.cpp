#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    int valor = 0; 
    cin >> n; 

    for (int i = 0; i < n; i++) {
        string instrucao;
        cin >> instrucao;

        if (instrucao.find("++") != string::npos) {
            valor++;
        } else if (instrucao.find("--") != string::npos) {
            valor--;
        }
    }

    cout << valor << endl;
    return 0;
}