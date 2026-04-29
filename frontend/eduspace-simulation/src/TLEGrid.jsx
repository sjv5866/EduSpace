import React, {useEffect, useState} from 'react';

export default function TLEGrid({name="POISK"}) {
    const [line1, setLine1] = useState('');
    const [line2, setLine2] = useState('');

    useEffect(() => {
        fetch(`http://localhost:5000/tles/${name}`)
          .then(res => res.json())
          .then(data => {
            setLine1(data.line1);
            setLine2(data.line2);
          });
    }, []);
    return (
        <div className='tleGrid'>
            <h3>{line1}</h3>
            <h3>{line2}</h3>
        </div>
    );
}