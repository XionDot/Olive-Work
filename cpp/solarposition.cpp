/*
Author: Xiondot
Date: 2022-12-21
*/

#include <cmath>
#include <iostream>

using namespace std;

int main() {
  double l, la;
  int y, mo, d, h, m, s, o;
  cout << "Enter longitude: ";
  cin >> l;
  cout << "Enter latitude: ";
  cin >> la;
  cout << "Enter year: ";
  cin >> y;
  cout << "Enter month: ";
  cin >> mo;
  cout << "Enter day: ";
  cin >> d;
  cout << "Enter hours: ";
  cin >> h;
  cout << "Enter minutes: ";
  cin >> m;
  cout << "Enter seconds: ";
  cin >> s;
  cout << "Enter UTC offset: ";
  cin >> o;

  // Calculate time in hours
  double t = h + m / 60.0 + s / 3600.0;

  // Adjust time for UTC offset
  t -= o;

  // Calculate Julian day
  // It is used as a reference point for celestial coordinates
  int N = 0;
  if (mo == 1 || mo == 2) {
    y -= 1;
    mo += 12;
  }
  if (y < 1582 || (y == 1582 && (mo < 10 || (mo == 10 && d <= 4)))) {
    N = -2;
  }
  double jd = floor(365.25 * y) + floor(30.6001 * (mo + 1)) + d + t / 24.0 + 1720994.5 + N;

  // Calculate sun's direction and elevation
  double declination = 0.4093 * sin((2 * M_PI * (jd - 81)) / 365.25);

  // The equation of time is a measure of the difference between time as measured by the sun and time as measured by a clock
  // It should take into account the elliptical shape of the Earth's orbit around the sun, the tilt of the Earth's axis, and the sun's apparent motion around the celestial equator
  double eqTime = 229.18 * (0.000075 + 0.001868 * cos(2 * M_PI * (jd - 81) / 365.25) - 0.032077 * sin(2 * M_PI * (jd - 81) / 365.25) - 0.014615 * cos(2 * M_PI * (jd - 81) / 365.25 - 2 * M_PI / 3) - 0.040849 * sin(2 * M_PI * (jd - 81) / 365.25 - 2 * M_PI / 3));
  // The hour angle is the angle between the sun and the celestial meridian
  double hourAngle = (12 - t - eqTime / 60 + o) * 15;
  double sunDir = 180 - hourAngle;
    // The sun's elevation is the angle between the sun and the horizon
  double sunElev = asin(sin(la * M_PI / 180) * sin(declination * M_PI / 180) + cos(la * M_PI / 180) * cos(declination * M_PI / 180) * cos(hourAngle * M_PI / 180)) * 180 / M_PI;

  // Normalize sun direction to range [0, 360]
  if (sunDir < 0) {
    sunDir += 360;
  }

  // Print sun's direction and elevation
  cout << "Sun's direction: " << sunDir << endl;
  cout << "Sun's elevation: " << sunElev << endl;

  return 0;
  }