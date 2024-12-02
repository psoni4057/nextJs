import {configureStore} from '@reduxjs/toolkit';
import modelReducer from './features/model-slice';
import { TypedUseSelectorHook,useSelector } from 'react-redux';

export const store = configureStore({
    reducer: {
       modelReducer,
}});
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;