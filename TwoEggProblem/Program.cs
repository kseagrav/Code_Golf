using System;

class TwoEggProblem
{
    static void Main(string[] args)
    {
        int numFloors = int.Parse(args[0]);
        int breakFloor = int.Parse(args[1]);

        int stepSize = (Convert.ToInt32(Math.Sqrt(1 + (8 * numFloors))) - 1) / 2;
        int remainder = (numFloors - ((stepSize * (stepSize + 1)) / 2));
        int lastGoodFloor = 0;
        int earliestBreak = numFloors + 1;
        bool repFlag = false;

        // traverse the building in leaps that are shrinking in size as we go up
        for(int tryLeap = stepSize; tryLeap < numFloors; tryLeap += stepSize) {
            Console.WriteLine(tryLeap);
            bool doesBreak = tryLeap >= breakFloor;
            Console.WriteLine(doesBreak);
            if (doesBreak) {
                earliestBreak = tryLeap;
                break;
            }
            lastGoodFloor = tryLeap;

            // handle the one case where you need to keep the step size constant
            if ((stepSize == remainder) && !repFlag) {
                repFlag = true;
            } else {
                --stepSize;
            }
        }

        // we found a floor on which the floor breaks, go to immediately above the
        // last floor that it did *not* break on and go 1 at a time until we hit
        // the earliest floor at which it breaks
        for (int tryFloor = (lastGoodFloor + 1); tryFloor < earliestBreak; ++tryFloor) {
            Console.WriteLine(tryFloor);
            bool doesBreak = tryFloor >= breakFloor;
            Console.WriteLine(doesBreak);
            if (doesBreak) {
                earliestBreak = tryFloor;
                break;
            }
        }

        Console.WriteLine("Floor " + earliestBreak);
    }
}

