class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        d=0
        originMass=mass
        def destroy(a):
            l,r=0,len(a)-1
            while(l<=r):
                m=(l+r)//2
                if(a[m]==mass):
                    return m
                elif(mass<a[m]):
                    r=m-1
                else:
                    l=m+1
            return l
        count={}
        for each in asteroids:
            if(each not in count):
                count[each]=1
            else:
                count[each]+=1
        asteroids=list(set(asteroids))
        asteroids.sort()
        s=[]
        tem=0
        d=set()
        for j in range(len(asteroids)):
            # stars.add(asteroids[j])
            tem+=asteroids[j]*count[asteroids[j]]
            s.append(tem)
        k=0
        while(k<len(asteroids)):
            targetI=destroy(asteroids)
            # if(targetI<0):
            #     return False
            print(targetI)
            while(targetI>=len(asteroids) or asteroids[targetI]>mass):
                targetI-=1
                if(targetI<0):
                    return False
            if(asteroids[targetI] not in d):
                # stars.remove(asteroids[targetI])
                d.add(asteroids[targetI])
                mass=originMass+s[targetI]
                k=targetI+1
            else:
                return False
        return True




class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in range(len(asteroids)):
            if(mass<asteroids[i]):
                return False
            else:
                mass+=asteroids[i]
        return True


sol=Solution()
mass = 10
asteroids = [3,9,19,5,21]
print(sol.asteroidsDestroyed(mass,asteroids))
