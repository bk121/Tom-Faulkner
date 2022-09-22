import React, {useState, useEffect} from "react";
import {Button, Form, TextArea, Segment} from "semantic-ui-react";
import './Textbox.css'
import {countryOptions, tradeOptions, furnitureOptions, modelOptions, shapeOptions, sizeOptions} from "../data/dropdowns"


const styleLink = document.createElement("link");
styleLink.rel = "stylesheet";
styleLink.href = "https://cdn.jsdelivr.net/npm/semantic-ui/dist/semantic.min.css";
document.body.appendChild(styleLink);


const Textbox = (props) => {

  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [country, setCountry] = useState("UK");
  const [tradeRetail, setTradeRetail] = useState("retail");
  const [furnitureType, setFurnitureType] = useState("dining");
  const [model, setModel] = useState("Angel");
  const [shape, setShape] = useState("Rectangular");
  const [size, setSize] = useState("M");
  

  const handleSubmit = ()=>{
    setInput(JSON.stringify({
      "country":country,
      "tradeRetail":tradeRetail,
      "furnitureType":furnitureType,
      "model":model,
      "shape":shape,
      "size":size, 
    }))
    console.log(input)
}

  useEffect(()=>{
    fetch("/data?"+new URLSearchParams({
      email: input,
  })).then((res) =>
      res.json().then((data) => {
          setOutput(data.text);
      })
    );
  }, [input])

  return (
    <div> 
      <p style={{color:'white', fontSize:45}}>TF Prices</p>
    <div style={{marginTop: '40px'}} >
    <Form onSubmit={handleSubmit} className="Info">
    <div style={{
    display: 'flex',
    justifyContent: 'center',
    height: '5vh', maxWidth:2000, }}>
    <Form.Dropdown value={country} onChange={(e, data)=>setCountry(data.value)} type='text' placeholder='Select Country' search selection options={countryOptions}/>
    <Form.Dropdown value={tradeRetail} onChange={(e, data)=>setTradeRetail(data.value)} type='text' placeholder='Select Trade/Retail'  search selection options={tradeOptions}/>
    <Form.Dropdown value={furnitureType} onChange={(e, data)=>setFurnitureType(data.value)} type='text' placeholder='Select Furniture Type'  search selection options={furnitureOptions}/>
    <Form.Dropdown value={model} onChange={(e, data)=>setModel(data.value)} type='text' placeholder='Select Model'  search selection options={modelOptions}/>
    <Form.Dropdown value={shape} onChange={(e, data)=>setShape(data.value)} type='text' placeholder='Select Shape'  search selection options={shapeOptions}/>
    <Form.Dropdown value={size} onChange={(e, data)=>setSize(data.value)} type='text' placeholder='Select Size'  search selection options={sizeOptions}/>
    </div>
      {/* <Form.TextArea name='text' icon='search' type="text" placeholder="Input email" style={{ minWidth: 1200, minHeight: 200 }}
      >
      </Form.TextArea>  */}
       <Button type='submit'>Submit</Button>
    </Form>
    <TextArea style={{ fontFamily: 'Monospace', position: 'relative', top: '40px', minWidth: 1600, minHeight: 170}} value={output} placeholder="Output" >
    </TextArea>
    </div>
    </div>
  );
}

export default Textbox

