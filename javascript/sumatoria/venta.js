


let AlmacenData = {
    "Producto 1": {"unidades": 100},
    "Producto 2": {"unidades": 40},
    "Producto 3": {"unidades": 30}
}


let ventaData = [{
    "id": "3WzFN",
    "cliente": "1",
    "nombre": "Vendedor 3",
    "total": 100,
    "lista": [{
            "unidades": "2",
            "precio": "25",
            "subtotal": 100,
            "producto": "Producto 1",
            "peso": "2"
            }]
},{
    "id": "6Zls",
    "cliente": "2",
    "nombre": "Vendedor1",
    "total": 550,
    "lista": [{
            "unidades": "4",
            "precio": "25",
            "subtotal": 100,
            "producto": "Producto 2",
            "peso": "2"
         }, {
            "unidades": "4",
            "precio": "25",
            "subtotal": 100,
            "producto": "Producto 1",
            "peso": "2"
         }],
},{
    "id": "U2HX",
    "cliente": "3",
    "nombre": "Vendedor2",
    "total": 600,
    "lista": [{
            "unidades": "2",
            "precio": "25",
            "subtotal": 100,
            "producto": "Producto 1",
            "peso": "2"
        }, {
            "unidades": "3",
            "precio": "25",
            "subtotal": 100,
            "producto": "Producto 3",
            "peso": "2"
        }]
}, {
    "id":"aJixp",
    "cliente":"4",
    "nombre": "Vendedor 3",
    "total": 220,
    "lista": [{
            "unidades": "2",
            "precio": "25",
            "subtotal": 100,
            "producto": "Producto 1",
            "peso": "2"
        }]
}]


function sumarVenta(ventaData) {
    // Sin utilizar reduce

    let item, subitem, result, d;
    let producto, unidades, subtotal;

    result = {};

    for(item of ventaData) {

        for(subitem of item.lista) {

            producto = subitem.producto;
            unidades = Number(subitem.unidades);
            subtotal = Number(subitem.subtotal);

            d = result[producto];
            if(!d)
                d = result[producto] = {"unidades": 0,
                                        "subtotal": 0};
            d["unidades"] += unidades;
            d["subtotal"] += subtotal;
        }

    }

    return result;
}


function restaAlmacen(almacenData, sumatoriaVentaData) {

    let d, unidadesVenta, unidadesAlmacen;
    for(let producto in sumatoriaVentaData)  {

        d = almacenData[producto];
        if(!d)
            throw new Error(`No existe el producto "${producto}" en el almacen`);

        unidadesVenta = sumatoriaVentaData[producto].unidades;
        unidadesAlmacen = d["unidades"];
            
        if(unidadesVenta > unidadesAlmacen)
            throw new Error(`No existen unidades disponibles del producto "${producto}"`);            

        d["unidades"] -= unidadesVenta;
    }
}


console.log("Almacen:", JSON.stringify(AlmacenData));

let sumatoriaVentaData = sumarVenta(ventaData);
restaAlmacen(AlmacenData, sumatoriaVentaData);

console.log("Venta:", JSON.stringify(sumatoriaVentaData));
console.log("Almacen:", JSON.stringify(AlmacenData));






//console.log(sumatoria(ventaData));

/*

El resultado que busco es: Producto 1 = 10. Producto 2 = 8. Producto 3 = 3. 

Almacen (Inicial)
Producto 1: {unidades: 100}
Producto 2: {unidades: 40}
Producto 3: {unidades: 30}

Venta
Producto 1: {unidades: 10, subtotal: 400}
Producto 2: {unidades: 4, subtotal: 100}
Producto 3: {unidades: 3, subtotal: 100}


Almacen (Final)
Producto 1: {unidades: 90}
Producto 2: {unidades: 36}
Producto 3: {unidades: 27}


*/





