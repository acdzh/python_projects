#include<iostream>
#include <sstream>
#include<windows.h>

using namespace std;

class Point{
	private:
		float _x;
		float _y;
	public:
		Point(float x, float y){
			_x = x;
			_y = y; 
		}
		float get_x(){
			return _x;
		}
		float get_y(){
			return _y;
		}
};

class a_swipe{
	private:
		float _ax;
		float _ay;
		float _bx;
		float _by;
	public:
		a_swipe(float ax, float ay, float bx, float by){
			_ax = ax;
			_ay = ay;
			_bx = bx;
			_by = by;
		}
		float get_ax(){
			return _ax;
		}
		float get_ay(){
			return _ay;
		}
		float get_bx(){
			return _bx;
		}
		float get_by(){
			return _by;
		}
};

void tap(Point a);
void tap(float x, float y);
void swipe(Point a, Point b);
void swipe(float ax, float ay, float bx, float by);
void swipe(a_swipe doing);
string convert(float number);

int main()
{
	Point back(39.7, 79.5);
	a_swipe up(252.3, 665.4, 260.7, 161.0);
	a_swipe down(260.7, 161.0, 252.3, 665.4);
	Point arts(255.5, 481.1);
	
	
	while(1){
		swipe(up);
		swipe(up);
		tap(arts);
		Sleep(1000);
		for(int i = 0; i < 5; i++){
			swipe(up);
			Sleep(300);
		} 
		Sleep(1000);
		tap(back);
	}
	
	
}

void tap(Point a){
	float x = a.get_x();
	float y = a.get_y();
	string adb_0 = "adb shell input tap ";
	string sx = convert(x);
	string sy = convert(y);
	string s = adb_0 + sx + " " + sy;
	cout << s << endl;
	const char *cstr = s.c_str();
	system(cstr);
}
void tap(float x, float y){
	string adb_0 = "adb shell input tap ";
	string sx = convert(x);
	string sy = convert(y);
	string s = adb_0 + sx + " " + sy;
	cout << s << endl;
	const char *cstr = s.c_str();
	system(cstr);
}

void swipe(Point a, Point b){
	float ax = a.get_x();
	float ay = a.get_y();
	float bx = b.get_x();
	float by = b.get_y();
	string adb_0 = "adb shell input swipe ";
	string sax = convert(ax);
	string say = convert(ay);
	string sbx = convert(bx);
	string sby = convert(by);
	string s = adb_0 + sax + " " + say + " " + sbx + " " + sby;
	cout << s << endl;
	const char *cstr = s.c_str();
	system(cstr);
}
void swipe(float ax, float ay, float bx, float by){
	string adb_0 = "adb shell input swipe ";
	string sax = convert(ax);
	string say = convert(ay);
	string sbx = convert(bx);
	string sby = convert(by);
	string s = adb_0 + sax + " " + say + " " + sbx + " " + sby;
	cout << s << endl;
	const char *cstr = s.c_str();
	system(cstr);
}
void swipe(a_swipe doing){
	float ax = doing.get_ax();
	float ay = doing.get_ay();
	float bx = doing.get_bx();
	float by = doing.get_by();
	string adb_0 = "adb shell input swipe ";
	string sax = convert(ax);
	string say = convert(ay);
	string sbx = convert(bx);
	string sby = convert(by);
	string s = adb_0 + sax + " " + say + " " + sbx + " " + sby;
	cout << s << endl;
	const char *cstr = s.c_str();
	system(cstr);
}
string convert(float number){
    std::ostringstream buff;
    buff<<number;
    return buff.str();   
}

