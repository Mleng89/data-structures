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

/*
hash.set('kyle',1)
console.log('this is the hash', hash)
console.log(hash.get('kyle'))

const hash = new Map()
let array = [1,1,1,1]
for(let i = 0 ; i< array.length;i++){
    if(!hash.has(array[i])){
        console.log(!hash.get(array[i]))
        hash.set(array[i], 1) 
    } else {
        const value = hash.get(array[i]) + 1
        hash.set(array[i], value)
    }
}
console.log('what is my hash', hash)
*/
