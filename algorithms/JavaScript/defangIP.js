/*
LEETCODE
--------
Given a valid (IPv4) IP address, returned a defanged version of that IP address

A defanged IP address replaces every '.' with '[.]'
*/
function defangIP(address) {
	return address.split('.').join('[.]');
}

module.exports = defangIP;
