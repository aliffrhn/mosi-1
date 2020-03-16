// gravitasi
let g = -9.806

// INPUTAN
// v(0)
let vnol = 50

// x(0)
let xnol = 0

// y(0)
let ynol = 0

// alfa
let alfa = 35

// delta t
const delta = 0.01

// define ax and ay
let ax = 0
let ay = g

// vx and vy
let dvx = vnol * Math.cos(alfa * 0.017453293)
// console.log("bla",(alfa/360) * (2*Math.PI))
// console.log("bla", Math.sin(alfa * 0.017453293))//jangan lupa ganti jadi 2π/360
let dvy = vnol * Math.sin(alfa * 0.017453293)

// function vx(t,dvx){
//     return dvx + (ax * delta)//ax*t bisa di jadiin const
// }

// function vy(t,dvy){
//     return dvy + (ay * delta)
// }

// define iterasi 0
// let xtnol = xnol + vx(t,dvx) * delta
// let ytnol = ynol + vy(t,dvy) * delta

// function xt(t){
//     return  + vx(t) * delta
// }

// t
var t,i = 0

// console.log(vy(t,dvy)+ " pass")
// console.log(ynol + " pass")
// console.log(delta + " pass")

// console.log("t "+ t)
// console.log(ynol)
// console.log(vy(t,dvy))


// console.log((ynol + (dvy * delta)))
// // aksmdkad
// console.log((ynol + (dvy * delta)) > 0)

let parameter = true

while(ynol>=0 && parameter){
        i++
        console.log("")
        console.log("")

        
        
        // x
        dvx = dvx + (ax * delta)
        

        xnol = xnol + (dvx * delta)
        
        
        // y
        dvy = dvy + (ay * delta)
        

        ynol = ynol + (dvy * delta)

        if(ynol<0){
            parameter = false
        }else {
            console.log("iterasi ke - ", i)
            console.log("Kecepatan Pada X = ", dvx)
            console.log("Posisi Pada X = ", xnol)
            console.log("Kecepatan Pada Y = ", dvy)
            console.log("Posisi Pada Y = ", ynol)
        }
        

        console.log("")
        console.log("")
        
    
}

