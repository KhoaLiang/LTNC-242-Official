// #include <iostream>

// using namespace std;
// class A {
//     void f() { cout << "A::f"; }
//     void f2() { f(); }
// };
    
// class B: public A {
//     void f() { cout << "B::f"; }
// };
    
// int main() {
//     A* a = new B();
//     a->f2();  // Output: ???
//     return 0;
// }
//--> inaccessable    

#include <iostream>

using namespace std;

class A {
protected:
    virtual void f() { cout << "A::f"; }
public:
    void f2() { f(); }
};

class B : public A {
protected:
    void f() override { cout << "B::f"; }
};

int main() {
    A* a = new B();
    a->f2();  // Output: B::f
    delete a; // Always clean up dynamically allocated memory
    return 0;
}