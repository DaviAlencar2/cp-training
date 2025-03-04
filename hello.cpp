#include <bits/stdc++.h>
using namespace std;
// iniciando estudos

int main() 
{
    int var = 100;
    cout << "num: " << var << endl;
    cout << "..." << endl;
    
    // leitura
    int reading1;
    string reading2;
    
    cin >> reading1 >> reading2;
    cout << reading1 << "," << reading2 << endl;
    
    // condicional
    
    if (reading1 % 2 == 0){
      cout << "reading1 -> par" << endl;
    }
    else{
      cout << "reading1 -> impar" << endl;
    }
    
    // repeticao
    
    for (int i = 0; i<reading2.size(); i++){
      cout << reading2[i] << endl;
    }
    
    
    return 0;
} 