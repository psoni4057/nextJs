import {createAction,createSlice,PayloadAction} from '@reduxjs/toolkit';


type InitialState = {
    value: ModelState;
}
type ModelState = {
    modelName: string;
    modelKey: string;
}
const initialState = {
    value: {
        modelName:'OpenAI',
        modelKey:''
    } as ModelState,
} as InitialState;

export const model = createSlice({
name: 'model',
initialState,
reducers: {
    setModelName: (state, action: PayloadAction<string>) => {
        state.value.modelName = action.payload;
    },
    setModelKey: (state, action: PayloadAction<string>) => {
        state.value.modelKey = action.payload;
    }
}
})

export const {setModelName,setModelKey} = model.actions;
export default model.reducer;