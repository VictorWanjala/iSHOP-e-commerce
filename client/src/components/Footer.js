import React from 'react'
import {FaTwitter} from 'react-icons/fa';
import {FaFacebookF} from 'react-icons/fa';
import {FaInstagram} from 'react-icons/fa';
import {FaLinkedin} from 'react-icons/fa';
import '../styles/Footer.css'

function Footer() {
  return (
    <div>
        <div className='socialMedia'>
        <FaTwitter/> <FaFacebookF/> <FaInstagram/> <FaLinkedin/>
        </div>
    </div>
  )
}

export default Footer