function Item({children, isGreen,age,add}){
    console.log(add);
    return(
        <li style={{"color": isGreen?"green":"red"}}>{children}, {age}</li>
    )
}

export default Item;