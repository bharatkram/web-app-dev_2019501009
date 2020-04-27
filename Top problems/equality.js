function deepEqual(obj1, obj2) {
    console.log("\n")
    console.log(obj1)
    console.log(obj2)
    if (typeof(obj1) == typeof(obj2)) {
        
        if (typeof(obj1) != "object")
            return obj1 === obj2
        
        if (obj1 == null && obj2 == null)
            return true
            
        if (obj1 != null && obj2 != null) {
            if (obj1 == null && obj2 == null)
                return true
            
            keys1 = Object.keys(obj1)
            keys2 = Object.keys(obj2)
            if (keys1.length != keys2.length)
                return false
            
            flag = true
            for (let i = 0; i < keys1.length; i++) {
                key = keys1[i]
                if (typeof(obj1[key]) != "object") {
                    if (obj1[key] === obj2[key]) {}
                    else {
                        flag = false
                        break
                    }
                } else {
                    temp = deepEqual(obj1[key], obj2[key])
                    if (!temp) {
                        flag = false
                        break
                    }
                }
            }
            return flag
        }
    }
    return false
}

obj2 = null
obj1 = null
obj3 = { a:1 }

console.log("\n***************\nTest for obj type and null:")
console.log(deepEqual(obj1, obj2))
console.log(deepEqual(obj1, obj3))

str1 = "Hello"
str2 = "Hello"
str3 = "hello"

int = 25
strint = "25"

console.log("\n***************\nTest for primitive datatypes")
console.log(deepEqual(str1, str2))
console.log(deepEqual(str1, str3))
console.log(deepEqual(str1, int))
console.log(deepEqual(int, strint))

obj4 = {a:1}
obj5 = {a:2}

console.log("\n***************\nTest for objects")
console.log(deepEqual(obj3, obj4))
console.log(deepEqual(obj4, obj5))

o1 = {a:1,b:{c:2}}
o2 = {a:1,b:{c:2}}
o3 = {a:1,b:{c:3}}
o4 = {a:1,b:{d:2}}
o5 = {a:1,e:{c:2}}

console.log("\n***************\nTest for objects containing objects")
console.log(deepEqual(o1, o2))
console.log(deepEqual(o1, o3))
console.log(deepEqual(o1, o4))
console.log(deepEqual(o1, o5))