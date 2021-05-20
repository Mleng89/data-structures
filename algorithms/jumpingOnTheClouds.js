/*
HACKER RANK
------------
There is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal to the 
number of the current cloud plus 1 or 2. The player must avoid the thunderheads. 
Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
*/

function jumpingOnClouds(c) {
	// Write your code here
	//set count variable
	let jumps = 0;
	//loop the array of clouds
	if (c.length === 2 || c.length === 3) return 1;

	let pointA = 0;
	let pointB = 1;
	while (pointA !== c.length - 1 || pointB < c.length - 1) {
		if (c[pointB] === 1) {
			pointB += 2;
			pointA += 2;
			jumps++;
		} else if (c[pointB] === 0) {
			if (c[pointB + 1] === 0) {
				pointB += 2;
				pointA += 2;
				jumps++;
			} else {
				pointA++;
				pointB++;
				jumps++;
			}
		}
	}

	//return count variable
	return jumps;
}

module.exports = jumpingOnClouds;
