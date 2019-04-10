// 1、注释的三种写法
    // console.log('注释')
    /* 区间注释*/
    /** 
     * 
     * 多行注释
     * 
    */

// 2、变量的定义
/*
console.log(b)

a = 100 // 不推荐使用
var b = 200 // 当前作用域提升此声明
let c = 300 // ES6语法
*/

// 3. 常量
/*
const d = 400
console.log(d)
*/

// 4、弱类型
/*
console.log('b' + 1)
console.log(a = 3 + 'magedu', typeof(a))
console.log(a = null + 'magedu', typeof(a))
console.log(a = undefined + 'magedu', typeof(a))
console.log(a = true + 'magedu', typeof(a))
*/

// 数字
/*
console.log(a = null + 8, typeof(a))
console.log(a = undefined + 8, typeof(a))
console.log(a = true + 8, typeof(a))
console.log(a = false + 8, typeof(a))
*/

// boolean
/*
console.log(a = null + true, typeof(a))
console.log(a = null + false, typeof(a))
console.log(undefined + true, typeof(a))
console.log(undefined + false, typeof(a))
console.log(null & true, typeof(a))
console.log(undefined & true, typeof(a))
*/
 // and or
 /*
 console.log(a = null && true, typeof(a))
 console.log(a = false && null, typeof(a))
 console.log(a = false && 'magedu', typeof(a))
 console.log(a = true && 'magedu', typeof(a))
 console.log(a = true && '', typeof(a))
*/

// 字符串
/*
var a = 100, b = 200;
s = `${a} : ${b}`
console.log(s)
*/


// 字符串
let school = 'magedu'
console.log(school.charAt(2))
console.log(school[2])
console.log(school.toUpperCase())
console.log(school.concat('.com'))
console.log(school.slice(3))
console.log(school.slice(3,5))
console.log(school.slice(-2.-1))
console.log(school.slice(-2))

let url = 'www.magedu.com'
console.log(url.split('.'))
console.log(url.substr(7,2))
console.log(url.substring(7,10))

let s = 'magedu.edu'
console.log(s.indexOf('ed'))
console.log(s.indexOf('ed',4))
console.log(s.replace('.edu','.com'))

s = ' \tmag edu \r\n'
console.log(s.trim())