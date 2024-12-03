const mongoose = require("mongoose")

mongoose.connect('mongodb://127.0.0.1:27017/sistemaEnergia');

const Medicion = mongoose.model('Medicion', { 
    voltaje: mongoose.Schema.Types.Decimal128,
    potencia: mongoose.Schema.Types.Decimal128,
    corriente: mongoose.Schema.Types.Decimal128
});

const medicion = new Medicion({
    voltaje: 45.32,
    potencia: 54.32,
    corriente: 534.32
})
medicion.save().then(() => console.log('meow'))