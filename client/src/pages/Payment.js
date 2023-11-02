import React, { useState } from 'react';
import '../styles/Payment.css'; 
import mpesaLogo from '../assets/mpesaLogo.png'

function Payment() {
  const [paymentMethod, setPaymentMethod] = useState('mpesa');
  const [paymentInfo, setPaymentInfo] = useState({
    mpesaNumber: '',
  });

  const handlePaymentMethodChange = (method) => {
    setPaymentMethod(method);
  };

  const handlePaymentInfoChange = (e) => {
    const { name, value } = e.target;
    setPaymentInfo({ ...paymentInfo, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
  
    console.log('Payment submitted', paymentMethod, paymentInfo);
  };

  return (
    <div className="payment-container">
      <h1>Payment Method</h1>
      <div className="payment-options">
        <img
          src={mpesaLogo}
          alt="M-Pesa"
          className={`payment-option ${paymentMethod === 'mpesa' ? 'active' : ''}`}
          onClick={() => handlePaymentMethodChange('mpesa')}
        />
      </div>

      <form className="payment-form" onSubmit={handleSubmit}>
        <input
          className='input'
          type="number"
          name="mpesaNumber"
          placeholder="M-Pesa Number"
          value={paymentInfo.mpesaNumber}
          onChange={handlePaymentInfoChange}
        />

        <button className='pay-button' type="submit">Pay Now</button>
      </form>
    </div>
  );
}

export default Payment;

