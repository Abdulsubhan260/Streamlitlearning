import streamlit as st


#  Layouts in streamlit



st.title("Columns Layout Example")

col1, col2 = st.columns(2)

col1.write("Left Column")
col1.button("Button 1")

col2.write("Right Column")
col2.button("Button 2")



# how to add image

st.title("Adding image")
st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQAogMBIgACEQEDEQH/xAAbAAEBAAMBAQEAAAAAAAAAAAAAAQIDBAUGB//EACoQAAIDAAEDAgYBBQAAAAAAAAABAgMRIQQSMQVBBhMiUVJhoRQzcYGx/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAECAwT/xAAZEQEBAQEBAQAAAAAAAAAAAAAAARECIRL/2gAMAwEAAhEDEQA/APxEAIrKgqAEKAAKQpQBSBAFAXUAAEBQBAygDEhX5IQAAAwy8DAAAKXABQE1AUYAKVEAgKkXAjFkM8JgVAXCA0IUA1i0TDIjIqAcFAAFRQKEUIhRhQiYEZBAMGGSRlgGKXAw2KJewqNLRMNrgRxIrWRmTIwMSMsnhjvGhQwk98CTMSa0awQEVtKiFRplSohkgyFBV5KKkXtM4xNsa9CNcYabFA3QrN0KW34KmueurfY2fJ48HdXSkjP5a+wZ15jq48HPbHD1rq0o+DzroNthdcTMWbpQNU+Fz5JW402PZE3jDHeSsy2rXJiVvhGJAAAVtKCo0zqoyMUUMqjZBGETfWipWyuJ01w011x06a+GVm1vpoTSOqNSXhGHT84dtdfcXGXI48mUYHVX00rro11LZNpJfdmE4OtuLTTTxp+Uy4OS6vVhxWUfo9VrTnuiTDXi3xVabZ5dsnKTZ6nqkku2HvJ6/wBJHkv+DFrtzBFZFw0R+TLYyAAAABuKCo0wFXkhkgjKKOmpGiKOipFiV1QSSN1UNZqrXCOymOFYrp6eHKPVrrXb/k4enS09r0yzoVNL1GrqJw/KiyMXn2xpp/waZ10fDfpV3qfrnSdNSn/cU5y/CKfLOP4pVM/iH1GfTZ8l9RNwzxmn0tnxR0vQ+m2dF8O+nvo/mx7bepsn3WyX+vB8fbHWCuOW4ctsk5OKacl5Xud04Yn7/ZHz8LN6ud00se9z3jF/0lWTXn+qTc+qmk+ILt4OOMdfLxFun3WTkuNlvBrbOdeiTwk98sgBFAAAAAG1TTM0aC6/uXWcb0VGiM2v2boy3lF1MbYnTUckWdEJlZruqaOyp+DzarOTupmsK516VMsOyuaSPLrsw3f1Ge5pHofMRhKaZxq/fcyduR0o0df1sKbFVOTj3Rb7l5R8z3/Pc5Sco93EVy8Rs6/qVb1lrl9XOLnwjjU/l8weSaaw52u3PONM815LTErZDDoAAAAAAAAoACBYvPBAB0RlpmpHKnnhm2uWmtZsdtUsOuFmHmwkzcrMLrFj0434jXZ1fYnKXscUbW3hr6ueqMfK3WXUkepR1UZviW/ozt6tOqxRf1JYuTxarZUx+lpOX3Wmm23hrh77k1r49YOfbPTBy0xBh1AAAAAAAAAABQAEAAAG54AA2xt/I2p6cpnXLHz4LqWOtS7Uabp/V7PEY2T8JGltvyLUnKyk5eSMgI2AAAAAAAAAAAAAKAAgAAoAAgGAFQAAAAAAAAAAAAAAAAAAf//Z",width =200)


 sidebar creation:




name=st.sidebar.text_input("what is your name: ")

role=st.sidebar.selectbox("choose your role:",["manager","boss",'python dev','full stack dev'])
if role:
    st.sidebar.success(f"you select your role as {role} ")


using st.expander

with st.expander("ingredients to make a Toast"):
    st.write(""" 
    1.  2 slices of bread

    2.    Butter or margarine

    3.    Jam, peanut butter, or toppings of your choice


""")


using st.container()

with st.container():
    st.write("This is inside a container")
    st.line_chart([1,2,3,4,5])



# simple project by using layouts





st.title("Simple Daily Planner")


st.sidebar.header("Your Info")
name = st.sidebar.text_input("Your Name")
day = st.sidebar.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])


st.image("https://images.unsplash.com/photo-1506784983877-45594efa4cbe?fit=crop&w=800&q=80", caption="Have a great day!", use_column_width=True)


st.header("Your Tasks")
morning, afternoon, evening = st.columns(3)

with morning:
    st.subheader("Morning")
    st.text_input("Task 1", key="Morning")
    


with evening:
    st.subheader(" Evening")
    st.text_input("Task 1", key="evening")
    


st.header("Tips")
with st.expander("Click for daily tips"):
    st.write(" Drink water regularly")
    st.write("Take short breaks while working")
    st.write("Stay positive and focused")


if name:
    st.write(f"Hello **{name}**, today is {day}. Have a good day")



#  *******Another simple project********** :


st.title("Simple player Chooser:")
name=st.sidebar.text_input("what is your name:")
nationality=st.sidebar.selectbox("choose your nationality",["Pakistani","indian","Bangladeshi","others"])
if name and nationality:
    st.sidebar.success("verified successfully!Now you can vote")

col1,col2=st.columns(2)
with col1:
    st.header("Babar Azam")
    st.image("data:image/jpeg;base64,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",width=200)
    vote1=st.button("vote for Babar Azam")


with col2:
    st.header("Virat Kohli")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIsZQYnc8FWICGpUA-2E62ED8bq35p0I7ErQ&s",width =200)
    vote2=st.button("vote for Virat kohli")

if vote1:
    st.success("you vote for Babar Azam")
    with st.expander("more info about Babar azam"):
        st.write(""" 
                 
        1. He is Pakistani
        2. one of the finest batsmen of the world
        3. 32* centuries in international career     


""")


elif vote2:
    st.success("you vote for Virat kohli")
    with st.expander("more info about Virat kohli"):
        st.write(""" 
                 
        1. He is indian
        2. one of the finest batsmen of the world
        3. 82 centuries in international career     


""")




