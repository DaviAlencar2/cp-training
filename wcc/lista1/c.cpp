#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int problemasResolvidos = 0;

    for (int i = 0; i < n; ++i) {
        int petya, vasya, tonya;
        cin >> petya >> vasya >> tonya;

        int contagem = petya + vasya + tonya;

        if (contagem >= 2) {
            problemasResolvidos++;
        }
    }

    cout << problemasResolvidos << endl;

    return 0;
}