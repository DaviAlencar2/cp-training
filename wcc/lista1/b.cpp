#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        string palavra;
        cin >> palavra;

        if (palavra.length() > 10) {
            cout << palavra[0] << palavra.length() - 2 << palavra[palavra.length() - 1] << endl;
        } else {
            cout << palavra << endl;
        }
    }

    return 0;
}