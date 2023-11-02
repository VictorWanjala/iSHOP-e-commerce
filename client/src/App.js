import React, { useState } from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Footer from './components/Footer';
import Register from './pages/Register';
import About from './pages/About';
import Login from './pages/Login';
import Cart from './pages/Cart';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    const updatedCart = [...cart];
    const productInCart = updatedCart.find((item) => item.id === product.id);

    if (productInCart) {
      productInCart.quantity++;
    } else {
      updatedCart.push({ ...product, quantity: 1 });
    }
    setCart(updatedCart);
  };

  const removeFromCart = (product) => {
    const updatedCart = cart.filter((item) => item.id !== product.id);
    setCart(updatedCart);
  };

  return (
    <div className="App">
      <Router>
        <Navbar cart={cart} />
        <Routes>
          <Route path="/" element={<Home addToCart={addToCart} />} />
          <Route path="/Register" element={<Register />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/About" element={<About />} />
          <Route path="/Cart" element={<Cart cart={cart} removeFromCart={removeFromCart} />} />
        </Routes>

        <Footer />
      </Router>
    </div>
  );
}

export default App;

