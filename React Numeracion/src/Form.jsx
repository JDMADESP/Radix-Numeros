import React, { useState } from 'react';
import axios from 'axios';

export default function SearchForm() {

    //Set number is the input
    //Set results is the output
  const [number, setNumber] = useState('');
  const [result, setResult] = useState('');

  const handleChange = (event) => {
    setNumber(event.target.value);
  };
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await axios.post("http://127.0.0.1:5000", {
    Numbers: [number]
    });
    setResult(response.data.Numbers[0]);
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="EnterNumber" id="Form">
        <label className="FormLabel">
          Enter Number:
          <input type="text" value={number} onChange={handleChange} />
        </label>
        <button type="submit">Search</button>
      </form>
      {result && <p>Result: {result}</p>}
    </>
  );
}

// import React, { useRef } from 'react';


// export default function Searchform(){ 
//     const [infor, infor_check] = useState();

    
//     return (<>
//         <form className="EnterNumber" id="Form">
//             <label className="FormLabel">
//                 Enter Number:
//                 <input type="text"/>
//             </label>
//             <button type="submit">Search</button>
//         </form>
//     </>);
// }////