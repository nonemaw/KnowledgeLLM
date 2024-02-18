import React from "react";
import { BaseProps } from "./Component";
import { twMerge } from "tailwind-merge";

export default function TextInput(
  props: BaseProps & {
    placeholder?: string;
    value?: string;
    onChange?: (newValue: string) => void;
  }
) {
  return (
    <input
      className={twMerge(
        "bg-textArea text-base p-1 rounded outline-none focus:ring  focus:border-active",
        props.className
      )}
      type="text"
      placeholder="Input title"
      value={props.value}
      onChange={(e) => props.onChange?.(e.target.value)}
    />
  );
}
