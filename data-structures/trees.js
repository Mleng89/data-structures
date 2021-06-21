//Trees

// Node class for a binary tree node
class TreeNode {
  constructor(value){
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Generate tree from array
function deserialize(arr) {
  if (arr.length === 0) { return null; }
  let root = new TreeNode(arr[0]);
  let queue = [root];
  for(let i = 1; i < arr.length; i += 2) {
    let current = queue.shift();
    if (arr[i] !== null) {
      current.left = new TreeNode(arr[i]);
      queue.push(current.left);
    }
    if (arr[i + 1] !== null && arr[i + 1] !== undefined) {
      current.right = new TreeNode(arr[i + 1]);
      queue.push(current.right);
    }
  }
  return root;
}

const array = [4, 2, 5, 1, 3, null, 7, null, null, null, null, 6, 8];
const treeNode = deserialize(array);
// console.log(treeNode);

/**
 *
 * Deserialize operates by building out the tree in a breadth-first
 * manner. One only needs to build down to the lowest row where there
 * exists nodes. For example, in this tree,
 *
 *          1
 *            \
 *              3
 *   				  /
 *   				 2
 *
 * The array that you would pass in to the deserialize function would
 * be [1,null,3,2,null]. The first null represents the left child of
 * the 1 node, and the second null represents the right child of the 3 node.
 *
 *  1. Here, we have built out the following tree using deserialize:
 *
 *              4
 *            /   \
 *          2       5
 *        /   \       \
 *      1       3       7
 *                    /   \
 *                  6      8
 */

//BREADTH FIRST traversal: [4,2,5,1,3,7,6,8]
function bfs(node) {
  let queue = [node]
  let result = []
  
  while(queue.length > 0) {
    let current = queue.shift()
    
    result.push(current.value)
    
    if(current.left !== null) { queue.push(current.left) }
    if(current.right !== null) { queue.push(current.right) }
    
  }
  
  return result
}


//PRE-ORDER DEPTH first traversal: [4,2,1,3,5,7,6,8]
let resultPre = []
function dfsPre(node) {
  if(node === null) { return; }
  
  resultPre.push(node.value)
  dfsPre(node.left)
  dfsPre(node.right)
  
  return resultPre
}


//IN-ORDER DEPTH first traversal: [1,2,3,4,5,6,7,8]
let resultIn = []
function dfsIn(node) {
  if(node === null) { return; }

  dfsIn(node.left)
  resultIn.push(node.value)
  dfsIn(node.right)
  
  return resultIn
}


//POST-ORDER DEPTH first traversal: [1,3,2,6,8,7,5,4]
let resultPost = []
function dfsPost(node) {
  if(node === null) { return; }

  dfsPost(node.left)
  dfsPost(node.right)
  resultPost.push(node.value)
  
  return resultPost
}


console.log(bfs(treeNode)) //[4,2,5,1,3,7,6,8]
console.log(dfsPre(treeNode)) //[4,2,1,3,5,7,6,8]
console.log(dfsIn(treeNode)) //[1,2,3,4,5,6,7,8]
console.log(dfsPost(treeNode)) //[1,3,2,6,8,7,5,4]