import React from 'react'
import Logo from '../assets/ISHOP.png'
import {FaShoppingCart} from 'react-icons/fa';
import { Link } from 'react-router-dom'
import '../styles/Navbar.css'

function Navbar() {
  return (
    <div className='navbar'>
        <div className='leftside'>
            <img src={Logo}/>
        <div className='hiddenLinks'>
            <Link to="/Register">Register</Link>
            <Link to="/Login">Login</Link>
        </div>
        </div>

    <div className='middle'>
        <input type="text" placeholder="Search" />
    </div>

        <div className='rightSide'>
            <Link to="/">Home</Link>
            <Link to="/About">About</Link>
            <Link to="/Register">Register</Link>
            <Link to="/Login">Login</Link>
            <Link to="/Cart">
                <FaShoppingCart size={30}/>
            </Link>
            
        </div>

    </div>
  )
}

export default Navbar