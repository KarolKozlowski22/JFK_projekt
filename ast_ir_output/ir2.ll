; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.-2452015952092396623" = private constant [4 x i8] c"%d\0a\00"
@".str.-774703926669740791" = private constant [4 x i8] c"%f\0a\00"
define void @"main"()
{
entry:
  %".2" = load i32, i32* @"first"
  %".3" = load i32, i32* @"second"
  %".4" = load i32, i32* @"first"
  %".5" = mul i32 %".3", %".4"
  %".6" = add i32 %".2", %".5"
  store i32 %".6", i32* @"first"
  %".8" = load i32, i32* @"first"
  %".9" = bitcast [4 x i8]* @".str.-2452015952092396623" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  ret void
}

@"first" = global i32 10
@"second" = global i32 5