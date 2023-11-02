import React from 'react'
import { useNavigate } from 'react-router-dom';
import '../styles/Cart.css'
import ReviewForm from './ReviewForm';

function Cart({cart, removeFromCart}) {
    const total = cart.reduce((acc, item)=>acc + item.price * item.quantity, 0);
    const navigate = useNavigate();
    const handleCheckout = () => {
      navigate('/payment');
    };
    const productId =  1

  return (
    <div className="cart-container">
    <h1 className="cart-header">Shopping Cart</h1>
    <table className="cart-table">
      <thead>
        <tr>
          <th>Product Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {cart.map((item, index) => (
          <tr key={index}>
            <td>{item.product_name}</td>
            <td>${item.price}</td>
            <td>{item.quantity}</td>
            <td>
              <button
                className="remove-button"
                onClick={() => removeFromCart(item)}
              >
                Remove
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
    <p className='total'>Total: ${total}</p>

    <button className="checkout-button" onClick={handleCheckout}>Checkout</button><br />
    <div><ReviewForm productId={productId} /></div>
  </div>


  )
}

export default Cart




