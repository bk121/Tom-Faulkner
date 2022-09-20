import React, {useState, useEffect} from "react";
import {Button, Form, TextArea} from "semantic-ui-react";
import './Textbox.css'

const Textbox = (props) => {

  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const handleSubmit = ({target})=>{
    setInput(target.text.value)
  }

  useEffect(()=>{
    fetch("/data?"+new URLSearchParams({
      email: input,
  })).then((res) =>
      res.json().then((data) => {
          setOutput(data.text);
          console.log(data.text)
      })
    );
  }, [input])

  return (
    <div>
    <Form onSubmit={handleSubmit} className="Textbox">
      <Form.TextArea name='text' icon='search' type="text" placeholder="Input email" style={{ minWidth: 1200, minHeight: 200 }}
      >
      </Form.TextArea>
      <Button type='submit'>Submit</Button>
    </Form>
    <TextArea value={output} placeholder="Output email" style={{ minWidth: 1200, minHeight: 200 }}>

    </TextArea>
    </div>
  );
}

export default Textbox