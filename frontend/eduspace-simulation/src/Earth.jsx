import { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';

export default function Earth(props) {
  const ref = useRef();
  const [earthTriangles, setEarthTriangles] = useState(32);
  const [rotate, setRotate] = useState(true);

  const texture = useMemo(() => new THREE.TextureLoader().load("./2k_earth_daymap.webp") ,[]);

  useEffect(() => {
    console.log(ref.current.geometry.uuid)
  })

  useFrame((_, delta) => {
    ref.current.rotation.y += 0.5 * delta * rotate
  })

  return (
  <mesh {...props} ref={ref} scale={[2, 2, 2]}>
    <sphereGeometry args={[1, earthTriangles, earthTriangles]} />
    <meshStandardMaterial attach="material" roughness={0.7}
          metalness={0.05} dithering={true}>
      <primitive attach="map" object={texture} />
    </meshStandardMaterial>
  </mesh>
  );
}