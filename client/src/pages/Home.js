import React from 'react'
import '../styles/Home.css'
import { useEffect, useState } from 'react';

function Home() {
    const [products, setProducts] = useState([]);
  
    useEffect(() => {
      fetch('/products')
        .then((response) => response.json())
        .then((products) => {
          setProducts(products);
          console.log(products)
        });
    }, []);
  
    return (
      <div className='products'>
        <div className='product-container'>
          {products.map((product, i) => (
            <div className='product-card' key={i}>
              <img src={product.image} />
              <h2>{product.product_name}</h2>
              <p>{product.description}</p>
              <p className='price'>$ {product.price}</p>
              <button className='buy-button'>Buy Now</button>

            </div>
          ))}
        </div>
      </div>
    );
  }
  
  export default Home;