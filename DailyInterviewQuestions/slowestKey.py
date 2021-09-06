class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowestKey,slowestDuration = keysPressed[0],releaseTimes[0]
        
        for i in range(1,len(keysPressed)):
            if(releaseTimes[i] - releaseTimes[i-1] > slowestDuration):
                slowestKey,slowestDuration = keysPressed[i],releaseTimes[i]-releaseTimes[i-1]
            elif(releaseTimes[i] - releaseTimes[i-1] == slowestDuration and ord(keysPressed[i])> ord(slowestKey)):
                slowestKey,slowestDuration = keysPressed[i],releaseTimes[i]-releaseTimes[i-1]
        
        return slowestKey
