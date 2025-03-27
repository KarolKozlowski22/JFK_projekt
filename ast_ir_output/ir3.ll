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
  %".2" = bitcast [4 x i8]* @".str.-2452015952092396623" to i8*
  %".3" = call i32 (i8*, ...) @"scanf"(i8* %".2", i32* @"x")
  %".4" = load i32, i32* @"x"
  %".5" = bitcast [4 x i8]* @".str.-2452015952092396623" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".4")
  ret void
}

@"x" = global i32 0