class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        Acan,Bcan=capacityA,capacityB
        A,B=0,len(plants)-1
        refill=0
        while(A<=B):
            if(A==B):
                if(Acan>=Bcan):
                    if(Acan<plants[A]):
                        refill+=1
                    # Acan-=plants[A]
                else:
                    if(Bcan<plants[A]):
                        refill+=1
                    # Bcan-=plants[A]
            else:
                if(Acan<plants[A]):
                    Acan=capacityA-plants[A]
                    refill+=1
                else:
                    Acan-=plants[A]
                
                if(Bcan<plants[B]):
                    Bcan=capacityB-plants[B]
                    refill+=1
                else:
                    Bcan-=plants[B]
                # Acan=Acan-plants[A] if Acan>=plants[A] else capacityA-plants[A]
                # Bcan=Bcan-plants[B] if Bcan>=plants[B] else capacityB-plants[B]
            A+=1
            B-=1
        return refill