/*

When trying to hash an array to keep track, reduce to an object:

array.reduce((accumulator,currentValue)=>{
    if(!accumulator[currentValue]){
        accumulator[currentValue] = 1
    } else{
        accumulator[currentValue] +=1
    }
  return accumulator
},{})

*/
