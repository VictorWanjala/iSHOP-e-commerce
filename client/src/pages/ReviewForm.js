import React, { useState } from 'react';
import '../styles/Review.css'

function ReviewForm({ productId }) {
  const [review, setReview] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    setReview('');
  };

  return (
    <div className="review-form">
      <h2>Add a Review</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Write your review here..."
          value={review}
          onChange={(e) => setReview(e.target.value)}
        ></textarea>
        <button type="submit">Submit Review</button>
        <button type="submit">Delete Review</button>
        <button type="submit">Update Review</button>
      </form>
    </div>
  );
}

export default ReviewForm;
