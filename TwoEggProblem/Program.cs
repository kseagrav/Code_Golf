﻿using System;

class T
{
    static void Main(string[] a)
    {
        int n = int.Parse(a[0]);
        int b = int.Parse(a[1]);

        int s = (Convert.ToInt32(Math.Sqrt(1 + (8 * n))) - 1) / 2;
        int r = (n - ((s * (s + 1)) / 2));
        int l = 0;
        int e = n + 1;
        bool f = false;

        for(int t = s; t < n; t += s) {
            Console.WriteLine(t);
            Console.WriteLine(t >= b);
            if (t >= b) {
                e = t;
                break;
            }
            l = t;

            if ((s == r) && !f) {
                f = true;
            } else {
                --s;
            }
        }

        for (int t = (l + 1); t < e; ++t) {
            Console.WriteLine(t);
            Console.WriteLine( t >= b);
            if ( t >= b) {
                e = t;
                break;
            }
        }

        Console.WriteLine("Floor " + e);
    }
}

